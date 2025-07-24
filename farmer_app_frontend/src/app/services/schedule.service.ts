import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { CreateSchedule, Schedule } from "../models/models";
import { environment } from "../../environments/environment";
import { Observable } from "rxjs";



@Injectable({
    providedIn:'root',
})
export class ScheduleService {

    constructor(private http: HttpClient){}

    getSchedulesDue(): Observable<Schedule[]> {
        const url= `${environment.apiBaseUrl}/schedules/due`;
        return this.http.get<Schedule[]>(url);
    }


    createSchedule(schedule: CreateSchedule): Observable<any> {
        const baseUrl = `${environment.apiBaseUrl}/schedule`;
        return this.http.post<any>(baseUrl, schedule);
    }
}

