import { Injectable }    from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import 'rxjs/add/operator/toPromise';
import { MyAuthService } from './my-auth.service';
import { Loan, LoanSerializer } from './loan';
import * as myGlobals from './globals'; //<==== this one

@Injectable()
export class LoanService {

  constructor(
    private http: Http,
    private myAuthService: MyAuthService) { }

  create(loan: Loan): Promise<Loan> {
    let url = myGlobals.backUrl + 'api/loans/';
    let loanSerializer = new LoanSerializer(loan);
    console.log(loanSerializer);
    let headers = new Headers({
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + this.myAuthService.token
    });
    return this.http
      .post(url, JSON.stringify(loanSerializer), {headers: headers})
      .toPromise()
      .then(res => res.json().data as Loan)
      .catch(this.handleError);
  }

  list(): Promise<Loan[]> {
    let url = myGlobals.backUrl + 'api/loans/';
    let headers = new Headers({
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + this.myAuthService.token
    });
    let options = new RequestOptions({ headers: headers });
    return this.http.get(url, options)
                .toPromise()
                .then(
                    response => {
                        return response.json() as Loan[]})
               .catch(this.handleError);
  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    console.log(error.status)
    return Promise.reject(error.message || error);
  }

}

