import { Injectable }    from '@angular/core';
import { Http, Headers, Response } from '@angular/http';
import 'rxjs/add/operator/map'
import 'rxjs/add/operator/toPromise';
import * as myGlobals from './globals'; //<==== this one

@Injectable()
export class MyAuthService {
    public token: string;
    private headers = new Headers({'Content-Type': 'application/json'});
    // URL to web api
    private loginUrl = myGlobals.backUrl + 'api-token-auth/';
    constructor(private http: Http) {
        var currentUser = JSON.parse(localStorage.getItem('currentUser'));
        this.token = currentUser && currentUser.token;
    }

    //curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api-token-auth/ -d '{ "username":"g.lourenco.santos@gmail.com", "password":"gui24830071993" }'
  login(username: string, password: string): Promise<any> {
    return this.http
      .post(
			this.loginUrl,
			JSON.stringify({username: username, password: password}),
			{headers: this.headers}
      )
      .toPromise()
      .then((response: Response) => {
       // login successful if there's a jwt token in the response
			let token = response.json() && response.json().token;
			if (token) {
				// set token property
				this.token = token;
				// store username and jwt token in local storage to keep
				//user logged in between page refreshes
				localStorage.setItem(
					'currentUser',
					 JSON.stringify({ username: username, token: token }));
				// return true to indicate successful login
				return true;
			} else {
				// return false to indicate failed login
				return false;
			}
      })
      .catch(this.handleError);
  }
  logout(): void {
	// clear token remove user from local storage to log user out
	this.token = null;
	localStorage.removeItem('currentUser');
  }
  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    console.log(error.status)
    return Promise.reject(error.message || error);
  }
}
