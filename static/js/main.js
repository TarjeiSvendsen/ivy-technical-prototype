function sendImage() {
  const url = `/uploadimage/?filter=${getSelectedFilter()}&alpha_strength=${
    document.getElementById("filter-intensity-slider").value
  }`;
  const formData = new FormData();
  formData.append(
    "image",
    document.getElementById("ivy-image-upload").files[0]
  );

  fetch(url, {
    method: "POST",
    body: formData,
  })
    .then((response) => {
      const reader = response.body.getReader();
      return new ReadableStream({
        start(controller) {
          return pump();
          function pump() {
            return reader.read().then(({ done, value }) => {
              // When no more data needs to be consumed, close the stream
              if (done) {
                controller.close();
                return;
              }
              // Enqueue the next data chunk into our target stream
              controller.enqueue(value);
              return pump();
            });
          }
        },
      });
    })
    // Create a new response out of the stream
    .then((stream) => new Response(stream))
    // Create an object URL for the response
    .then((response) => response.blob())
    .then((blob) => URL.createObjectURL(blob))
    // Update image
    .then((url) => console.log((downloadImage(url,document.getElementById("ivy-image-upload").files[0].name) )))
    .catch((err) => console.error(err));
}

function downloadImage(image_url,filename) {
  let _download_a = document.createElement("a");
  _download_a.href = image_url;
  _download_a.download = filename;
  _download_a.target = "_blank";
  _download_a.click();
  
}

function getSelectedFilter() {
  let radioButtons = document.getElementsByName("filter-selection");

  radioButtons.forEach((radioButton) => {
    if (radioButton.id == "bw-filter") {
      return "bw-filter";
    } else if (radioButton.id == "bw-filter") {
      return "colour-filter";
    }
  });
}
