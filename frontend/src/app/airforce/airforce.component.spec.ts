import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AirforceComponent } from './airforce.component';

describe('AirforceComponent', () => {
  let component: AirforceComponent;
  let fixture: ComponentFixture<AirforceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AirforceComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AirforceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
