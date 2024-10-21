import {} from "./p5.js";

export function captureImages() {
  let images = document.getElementById("ivy-image-choice").files;
  console.log(images);
}

export function alterImage(image){
  
}

export function determineServerOrClientRenderer() {
  let choice = document.getElementById("ivy-render-choice");
}

export function getLicenceStatus() {
  let licenceLocalStorageFile = localStorage.getItem("LicenceStatus");
  if (licenceLocalStorageFile == null) {
    return "You either don't have a licence or you haven't imported it.";
  } else {
    return "Your licence is valid.";
  }
}

export function setLicence() {

}

export function activateLicence(){
    let licenceBodyData = new FormData();
    licenceBodyData.append("",)
    let remoteLicenceStatus = fetch("/uploadimage",{body:licenceBodyData})
}