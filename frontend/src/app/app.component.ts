import { HttpClient } from '@angular/common/http';
import {Component} from '@angular/core';
import { MatIconRegistry } from "@angular/material/icon";
import { DomSanitizer } from "@angular/platform-browser";


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  data_from_month = "August";

  constructor(
    private matIconRegistry: MatIconRegistry,
    private domSanitizer: DomSanitizer,
    public http : HttpClient
    )
    {
    this.matIconRegistry.addSvgIcon(
      "army_icon",
      this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/img/army_icon.svg")
    );

    this.matIconRegistry.addSvgIcon(
      "airforce_icon",
      this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/img/airforce_icon.svg")
    );

    this.matIconRegistry.addSvgIcon(
      "navy_icon",
      this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/img/navy_icon.svg")
    );

    this.matIconRegistry.addSvgIcon(
      "marinecorps_icon",
      this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/img/marinecorps_icon.svg")
    );

    this.matIconRegistry.addSvgIcon(
      "coastguard_icon",
      this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/img/coastguard_icon.svg")
    );
  }
}
