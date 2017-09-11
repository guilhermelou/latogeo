import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CurrentLoansComponent } from './current-loans.component';

describe('CurrentLoansComponent', () => {
  let component: CurrentLoansComponent;
  let fixture: ComponentFixture<CurrentLoansComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CurrentLoansComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CurrentLoansComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
