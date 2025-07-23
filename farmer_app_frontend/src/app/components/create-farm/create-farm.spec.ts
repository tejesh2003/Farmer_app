import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateFarm } from './create-farm';

describe('CreateFarm', () => {
  let component: CreateFarm;
  let fixture: ComponentFixture<CreateFarm>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CreateFarm]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateFarm);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
