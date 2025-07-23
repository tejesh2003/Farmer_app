import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Getbill } from './getbill';

describe('Getbill', () => {
  let component: Getbill;
  let fixture: ComponentFixture<Getbill>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Getbill]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Getbill);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
