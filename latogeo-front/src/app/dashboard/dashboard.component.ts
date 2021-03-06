import { Component, OnInit } from '@angular/core';

import { Observable }        from 'rxjs/Observable';
import { Subject }           from 'rxjs/Subject';
import { Item, ItemKind, ItemSpec } from './../item';
import { ItemService } from './../item.service';
import { UserPub } from './../user';
import { UserService } from './../user.service';
import { Course, Discipline } from './../course';
import { CollegeService } from './../college.service';
import { Loan } from './../loan';
import { LoanService } from './../loan.service';
//getCourses
// Observable class extensions
import 'rxjs/add/observable/of';

import 'rxjs/add/operator/switchMap';

// Observable operators
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/distinctUntilChanged';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  loan: Loan;
  kinds: ItemKind[];
  students: Observable<UserPub[]>;
  studentStr: string;
  professors: UserPub[];
  courses: Course[];
  private searchStudentsTerms = new Subject<string>();
  private searchProfessorsTerms = new Subject<string>();

    constructor(
        private itemService: ItemService,
        private userService: UserService,
        private collegeService: CollegeService,
        private loanService: LoanService
    ) { }

  getKinds(): void {
    this.itemService
        .getKinds()
        .then(kinds => this.kinds = kinds);
  }

  getProfessors(): void {
      this.userService.getProfessors().then(users => this.professors=users);
  }

  searchStudents(term: string): void {
    this.searchStudentsTerms.next(term);
  }

  searchProfessors(term: string): void {
    this.searchProfessorsTerms.next(term);
    console.log(this.loan.disciplineSelected);
    console.log(this.loan.removalPlannedDate);
  }

  ngOnInit() {
    this.loan = new Loan();
    console.log(this.loan);
    this.getKinds();
    this.getCourses();
    this.getProfessors();
      //this.loan.itemsSelected = new Array<Item>();
      //this.loan.studentsSelected = new Array<UserPub>();
    this.students = this.searchStudentsTerms
      // wait 300ms after each keystroke before considering the term
      .debounceTime(300)
      // ignore if next search term is same as previous
      .distinctUntilChanged()
      // switch to new observable each time the term changes
      .switchMap(term => term
        // return the http search observable
        ? this.userService.search(term)
        // or the observable of empty heroes if there was no search term
        : Observable.of<UserPub[]>([]))
            .catch(error => {
                //add real error handling
                console.log(error);
                return Observable.of<UserPub[]>([]);
            });
  }

  // This Method add a item from a selected spec to the list of items selected
  onSelectSpec(kind: ItemKind, spec: ItemSpec): void{
    let item = spec.items_available.pop();
    if (item!=null){
        item.kind = kind;
        item.spec = spec;
        this.loan.itemsSelected.push(item);
    }
  }
  onRemoveItem(item: Item): void{
    item.spec.items_available.push(item);
    this.loan.itemsSelected = this.loan.itemsSelected.filter(h => h !== item);
  }
  addStudent(user: UserPub): void {
    this.studentStr = '';
    this.searchStudents('');
    this.removeStudent(user);
    this.loan.studentsSelected.push(user);
  }
  removeStudent(user: UserPub): void {
      this.loan.studentsSelected = this.loan.studentsSelected.filter(
          h => h.id !== user.id);
  }
  getCourses(): void {
    this.collegeService
        .getCourses()
        .then(courses => this.courses = courses);
  }
  selectDiscipline(discipline: Discipline): void {
    this.loan.disciplineSelected = discipline;
      console.log("escolheu");
  }
  createLoan(): void{
    console.log("AGENDAR");
    console.log(this.loan);
    this.loanService
        .create(this.loan)
        .then(loan => console.log(loan));
  }
}
