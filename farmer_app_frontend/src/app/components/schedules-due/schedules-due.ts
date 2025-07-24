import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { Schedule } from '../../models/models';
import { ScheduleService } from '../../services/schedule.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-schedules-due',
  standalone:true,
  imports: [CommonModule],
  templateUrl: './schedules-due.html',
  styleUrl: './schedules-due.css'
})
export class SchedulesDue implements OnInit{
  schedules : Schedule[] = [];

  constructor(private scheduleService: ScheduleService, private cdr: ChangeDetectorRef){}

  ngOnInit(): void {
    this.scheduleService.getSchedulesDue().subscribe({
      next: (data)=> {
        this.schedules=data
        this.cdr.detectChanges();
      },
      error: (err) => console.error('Failed to fetch schedules', err),
    });
  }


}
