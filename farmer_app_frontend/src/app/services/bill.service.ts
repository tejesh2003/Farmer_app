import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { FarmerBill } from "../models/models";
import { environment } from "../../environments/environment";



@Injectable({
    providedIn: 'root',
})
export class BillService {

    constructor(private http: HttpClient){}

    getBill(farmerId: number, fertilizerPrices: { [key: string]: number }): Observable<FarmerBill>{
        const url = `${environment.apiBaseUrl}/bill/${farmerId}`;
        return this.http.post<FarmerBill>(url,fertilizerPrices);
    }
}