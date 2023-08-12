import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoastguardComponent } from './coastguard.component';

describe('CoastguardComponent', () => {
  let component: CoastguardComponent;
  let fixture: ComponentFixture<CoastguardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CoastguardComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CoastguardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
