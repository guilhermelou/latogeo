import { Injectable }    from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import 'rxjs/add/operator/toPromise';
import { MyAuthService } from './my-auth.service';
import { Course, Discipline } from './course';
import * as myGlobals from './globals'; //<==== this one

@Injectable()
export class CollegeService {

  constructor(
    private http: Http,
    private myAuthService: MyAuthService) { }

  getCourses(): Promise<Course[]> {
    let url = myGlobals.backUrl + 'api/courses/';
    let headers = new Headers({
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + this.myAuthService.token
    });
    let options = new RequestOptions({ headers: headers });
    return this.http.get(url, options)
                .toPromise()
                .then(
                    response => {
                        console.log(response.json());
                        return response.json() as Course[]})
            .catch(this.handleError);
  }
  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    console.log(error.status)
    return Promise.reject(error.message || error);
  }
}




