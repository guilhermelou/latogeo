import { Injectable }    from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import 'rxjs/add/operator/toPromise';
import { MyAuthService } from './my-auth.service';
import { Item, ItemKind, ItemSpec } from './item';
import * as myGlobals from './globals'; //<==== this one

@Injectable()
export class ItemService {

    //private heroesUrl = 'api/heroes';  // URL to web api

  constructor(
    private http: Http,
    private myAuthService: MyAuthService) { }

  getItems(): Promise<Item[]> {
    let url = myGlobals.backUrl + 'api/items/';
    let headers = new Headers({
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + this.myAuthService.token
    });
    let options = new RequestOptions({ headers: headers });
    return this.http.get(url, options)
                .toPromise()
                .then(
                    response => {
                        return response.json() as Item[]})
               .catch(this.handleError);
  }

  getKinds(): Promise<ItemKind[]> {
    let url = myGlobals.backUrl + 'api/items/kinds/';
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
                        return response.json() as ItemKind[]})
            .catch(this.handleError);
  }
/*
  getHero(id: number): Promise<Hero> {
    const url = `${this.heroesUrl}/${id}`;
    return this.http.get(url)
      .toPromise()
      .then(response => response.json().data as Hero)
      .catch(this.handleError);
  }
*/
  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    console.log(error.status)
    return Promise.reject(error.message || error);
  }
}
