import { Item, ItemKind, ItemSpec } from './item';
import { UserPub } from './user';
import { Course, Discipline } from './course';

function toISO(dateStr) {
    var parts = dateStr.split("/");
    return parts[2]+"-"+parts[1]+"-"+parts[0];
}


export class Loan {
  itemsSelected: Item[];
  studentsSelected: UserPub[];
  professorSelected: UserPub;
  disciplineSelected: Discipline;
  removalPlannedDate: string;
  deliveryPlannedDate: string;
  external: boolean;
  constructor(){
    this.external = false;
    this.itemsSelected = new Array<Item>();
    this.studentsSelected = new Array<UserPub>();

  }
}


export class LoanSerializer {
    students: number[];
    professor: number;
    removal_planned_date: string;
    delivery_planned_date: string;
    terms = true;
    status = 0;
    items: number[];
    external: boolean;
    discipline: number;
    constructor(loan: Loan){
        this.students = loan.studentsSelected.map(h => h.id);
        this.items = loan.itemsSelected.map(h => h.id);
        this.professor = loan.professorSelected.id;
        this.removal_planned_date = toISO(loan.removalPlannedDate);
        this.delivery_planned_date = toISO(loan.deliveryPlannedDate);
        this.external = loan.external;
        this.discipline = loan.disciplineSelected.id;
    }
}

