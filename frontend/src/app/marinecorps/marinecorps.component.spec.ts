import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MarinecorpsComponent } from './marinecorps.component';

describe('MarinecorpsComponent', () => {
  let component: MarinecorpsComponent;
  let fixture: ComponentFixture<MarinecorpsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MarinecorpsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MarinecorpsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
