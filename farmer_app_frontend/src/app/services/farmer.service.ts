import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable, map } from "rxjs";
import { environment } from "../../environments/environment";
import { CreateFarmer, Farmer } from "../models/models";

@Injectable({
  providedIn: "root",
})
export class FarmerService {
  private baseUrl = environment.apiBaseUrl;

  constructor(private http: HttpClient) {}

  createFarmer(farmer: CreateFarmer): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/farmer`, farmer);
  }

  getFarmersByCrop(crop: string): Observable<Farmer[]> {
    const url = `${this.baseUrl}/farmers/by-crop?crop=${encodeURIComponent(crop)}`;
    return this.http.get<any[]>(url).pipe(map(this.transformFarmers));
  }

  getFarmersWithCrop(): Observable<Farmer[]> {
    const url = `${this.baseUrl}/farmers/with-crop`;
    return this.http.get<any>(url);
  }

  getAllFarmers(): Observable<any> {
    const url = `${this.baseUrl}/all-farmers`;
    return this.http.get<any>(url);
  }

  private transformFarmers = (data: any[]): Farmer[] =>
    data.map(farmer => ({
      id: farmer.id,
      name: farmer.name,
      phone: farmer.phone,
      language: farmer.language,
      country: farmer.country,
      farm_ids: Array.isArray(farmer.farms) ? farmer.farms.map((f: any) => f.id) : [],
    }));
}
