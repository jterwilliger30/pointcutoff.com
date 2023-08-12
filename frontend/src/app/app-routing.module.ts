import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ArmyComponent } from './army/army.component';
import { NavyComponent } from './navy/navy.component';
import { CoastguardComponent } from './coastguard/coastguard.component';
import { MarinecorpsComponent } from './marinecorps/marinecorps.component';
import { AirforceComponent } from './airforce/airforce.component';

const routes: Routes = [
  { path: "army", component: ArmyComponent },
  { path: "navy", component: NavyComponent },
  { path: "coastguard", component: CoastguardComponent },
  { path: "marinecorps", component: MarinecorpsComponent },
  { path: "airforce", component: AirforceComponent },
  { path: "", redirectTo: "/army", pathMatch: "full" }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
