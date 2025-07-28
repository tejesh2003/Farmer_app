import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AllFarmers } from './all-farmers';

describe('AllFarmers', () => {
  let component: AllFarmers;
  let fixture: ComponentFixture<AllFarmers>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AllFarmers]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AllFarmers);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
