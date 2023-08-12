import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { Component } from '@angular/core';
import { FormControl } from '@angular/forms';
import {map, startWith} from 'rxjs/operators';


@Component({
  selector: 'app-army',
  templateUrl: './army.component.html',
  styleUrls: ['./army.component.css']
})
export class ArmyComponent {
  army_mos_list_url = "http://localhost:5001/mos_list";
  army_points_url = "http://localhost:5001/army_handle_data";

  selectedVal : string = '';
  filteredOptions : Observable<string[]>;
  control = new FormControl();
  options : string[] = [];

  input : string;
  selection : string;

  data : any;
  show_data = false;

  constructor(private http : HttpClient) {}


  ngOnInit() {
    
  }

  get_MOS_points()
  {
    this.http.post<string[]>(this.army_points_url, {mos: this.input, component_selector: this.selectedVal}).subscribe(
      (response)  => {
        this.data = response;
        this.show_data = true;
       }, (error) => {
        this.show_data = false;
       }
    );
  }


  public onValChange(val: string) {
    this.selectedVal = val;
    this.get_MOS_List();
  }

  get_MOS_List()
  {
    this.http.post<string[]>(this.army_mos_list_url, {component_selector: this.selectedVal}).subscribe(
      (response)  => {
        this.options = response;
        this.filter();
       }
    );
  }

  public filter() {
    this.filteredOptions = this.control.valueChanges.pipe(
      startWith(''), map(value => this._filter(value || '')));
  }

  private _filter(value: string): string[] {
    const filterValue = value.toLowerCase();
    return this.options.filter(option => option.toLowerCase().includes(filterValue));
  }
  
}
