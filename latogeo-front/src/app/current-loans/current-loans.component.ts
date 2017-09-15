import { Component, OnInit } from '@angular/core';

//import { Item, ItemKind, ItemSpec } from './../item';
import { UserPub } from './../user';
import { Course, Discipline } from './../course';
import { Loan } from './../loan';
import { LoanService } from './../loan.service';

// Observable class extensions
import 'rxjs/add/observable/of';

import 'rxjs/add/operator/switchMap';

// Observable operators
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/debounceTime';
import 'rxjs/add/operator/distinctUntilChanged';

@Component({
  selector: 'app-current-loans',
  templateUrl: './current-loans.component.html',
  styleUrls: ['./current-loans.component.css']
})

export class CurrentLoansComponent implements OnInit {

  currentLoans: Loan[];
  constructor(
        private loanService: LoanService
  ) { }

  updateCurrentLoans(): void {
    this.loanService
        .list()
        .then(loans => {this.currentLoans = loans; console.log(this.currentLoans)});
  }

  cancelLoan(id: number): void {
    this.loanService
		.cancel(id)
		.then(loan => console.log(loan));

  }
  ngOnInit() {
    this.updateCurrentLoans();
  }
}

