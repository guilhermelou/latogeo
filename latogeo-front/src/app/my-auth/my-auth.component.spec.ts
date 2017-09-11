import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MyAuthComponent } from './my-auth.component';

describe('MyAuthComponent', () => {
  let component: MyAuthComponent;
  let fixture: ComponentFixture<MyAuthComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MyAuthComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MyAuthComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
