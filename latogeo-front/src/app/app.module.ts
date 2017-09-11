import { MaterializeModule } from 'angular2-materialize';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { FormsModule }   from '@angular/forms';
import { HttpModule }    from '@angular/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MyAuthComponent } from './my-auth/my-auth.component';
import { MyAuthService } from './my-auth.service';
import { MyAuthGuard } from './my-auth/my-auth.guard';
import { ItemService } from './item.service';
import { UserService } from './user.service';
import { CollegeService } from './college.service';
import { LoanService } from './loan.service';
import { DashboardComponent } from './dashboard/dashboard.component';
import { FilterPipe } from './filter.pipe';
import { LoanComponent } from './loan/loan.component';
import { CurrentLoansComponent } from './current-loans/current-loans.component';
import { HistoryLoansComponent } from './history-loans/history-loans.component';

@NgModule({
  declarations: [
    AppComponent,
	FilterPipe,
    MyAuthComponent,
	DashboardComponent,
	LoanComponent,
	CurrentLoansComponent,
	HistoryLoansComponent,
  ],
  imports: [
  	MaterializeModule,
    BrowserModule,
    FormsModule,
    HttpModule,
    AppRoutingModule
  ],
    providers: [
        MyAuthService, MyAuthGuard, ItemService, UserService, CollegeService,
        LoanService ],
  bootstrap: [AppComponent]
})
export class AppModule { }
