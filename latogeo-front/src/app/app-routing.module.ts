import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MyAuthComponent }  from './my-auth/my-auth.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MyAuthGuard } from './my-auth/my-auth.guard';
const routes: Routes = [
  { path: 'login', component: MyAuthComponent },
  { path: 'dashboard', component: DashboardComponent, canActivate: [MyAuthGuard] },

];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}

