import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FarmersWithCrop } from './farmers-with-crop';

describe('FarmersWithCrop', () => {
  let component: FarmersWithCrop;
  let fixture: ComponentFixture<FarmersWithCrop>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FarmersWithCrop]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FarmersWithCrop);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
