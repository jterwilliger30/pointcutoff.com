import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavyComponent } from './navy.component';

describe('NavyComponent', () => {
  let component: NavyComponent;
  let fixture: ComponentFixture<NavyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NavyComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NavyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
