export class Discipline {
    id: number;
    name: string;
    cod: string;
}
export class Course {
    id: number;
    name: string;
    cod: string;
    course_discipline: Discipline[] = [];
}
