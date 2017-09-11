import { Component, OnInit } from '@angular/core';
import { MyAuthService } from './../my-auth.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-my-auth',
  templateUrl: './my-auth.component.html',
  styleUrls: ['./my-auth.component.css']
})
export class MyAuthComponent implements OnInit {

  constructor(private myAuthService: MyAuthService, private router: Router) { }

  ngOnInit() {
      this.myAuthService.logout();
  }

  login(loginStr: string, passwordStr: string): void {
      console.log("clicou");
    this.myAuthService.login(loginStr, passwordStr)
      .then(res => {
			let link = ['/dashboard'];
			this.router.navigate(link);
      });
  }
}
