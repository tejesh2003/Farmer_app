import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FarmersByCrop } from './farmers-by-crop';

describe('FarmersByCrop', () => {
  let component: FarmersByCrop;
  let fixture: ComponentFixture<FarmersByCrop>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FarmersByCrop]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FarmersByCrop);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
