import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import 'rxjs/add/operator/toPromise';
import { MyAuthService } from './my-auth.service';
import { UserPub } from './user';
import { Observable }     from 'rxjs/Observable';
import * as myGlobals from './globals'; //<==== this one

@Injectable()
export class UserService {

  constructor(
    private http: Http,
    private myAuthService: MyAuthService) { }

  search(term: string): Observable<UserPub[]> {
    let url = myGlobals.backUrl + 'api/users/?search='+term;
    console.log(url);
    let headers = new Headers({
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + this.myAuthService.token
    });
    let options = new RequestOptions({ headers: headers });
    return this.http.get(url, options)
      .map(response => {
          console.log(response.json());
          return response.json() as UserPub[]
      });
  }

  getProfessors(): Promise<UserPub[]> {
    let url = myGlobals.backUrl + 'api/users/professors_or_chiefs/';
    let headers = new Headers({
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + this.myAuthService.token
    });
    let options = new RequestOptions({ headers: headers });
    return this.http.get(url, options)
                .toPromise()
                .then(
                    response => {
                        return response.json() as UserPub[]})
               .catch(this.handleError);
  }
  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    console.log(error.status)
    return Promise.reject(error.message || error);
  }
}
