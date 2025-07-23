import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SchedulesDue } from './schedules-due';

describe('SchedulesDue', () => {
  let component: SchedulesDue;
  let fixture: ComponentFixture<SchedulesDue>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SchedulesDue]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SchedulesDue);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
