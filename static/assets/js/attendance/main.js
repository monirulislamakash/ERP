let markAttendance = () => {
  let progressBar = document.querySelector('.progress-bar');
  document.getElementById('Mark_AttendanceText').innerText = "Getting location, please wait...";
  document.getElementById('progress').style.display = "block";
  progressBar.style.width = '0%'; // Reset progress bar

  document.getElementById('Mark_AttendanceText').innerText = "Location obtained. Marking attendance...";
  setTimeout(() => {
    progressBar.style.width = '100%';
  }, 500);
  setTimeout(() => {
    document.getElementById('submitFrom').submit();
  }, 2000);


  // let attempts = 0;
  // const maxAttempts = 1; // Try a few times
  // const desiredAccuracy = 50; // In meters, e.g., aiming for 50m accuracy

  // const getLocation = () => {
  //     navigator.geolocation.getCurrentPosition(
  //         (position) => {
  //             const currentAccuracy = position.coords.accuracy;
  //             console.log("Current accuracy:", currentAccuracy, "meters");

  //             if (currentAccuracy <= desiredAccuracy || attempts >= maxAttempts) {
  //                 // Either accurate enough, or ran out of attempts
  //                 document.getElementById('latitude').value = position.coords.latitude;
  //                 document.getElementById('longitude').value = position.coords.longitude;

  //                 document.getElementById('Mark_AttendanceText').innerText = "Location obtained. Marking attendance...";
  //                 setTimeout(() => {
  //                     progressBar.style.width = '100%';
  //                 }, 500);
  //                 setTimeout(() => {
  //                     document.getElementById('submitFrom').submit();
  //                 }, 2000); // Shorter delay after location is confirmed
  //             } else {
  //                 // Not accurate enough, try again
  //                 attempts++;
  //                 document.getElementById('Mark_AttendanceText').innerText = `Improving accuracy... Attempt ${attempts} of ${maxAttempts}`;
  //                 setTimeout(getLocation, 2000); // Wait 2 seconds before retrying
  //             }
  //         },
  //         (error) => {
  //             console.error("Geolocation error:", error);
  //             document.getElementById('Mark_AttendanceText').innerText = "Could not get location. Error: " + error.message;
  //             // Optionally hide progress bar or show an error state
  //             document.getElementById('progress').style.display = "none";
  //         },
  //         {
  //             enableHighAccuracy: true, // Request best possible accuracy
  //             timeout: 10000,          // Give it 10 seconds to get a fix
  //             maximumAge: 0            // Don't use a cached position, always get fresh
  //         }
  //     );
  // };

  // getLocation(); // Start the process
};
let toaster = () => {
  let toast = document.querySelector('.toast')
  toast.style.display = "none";
}
setTimeout(() => {
  let toast = document.querySelector('.toast')
  toast.style.display = "none";
}, 5000)


// const options = {
//   enableHighAccuracy: true,
//   timeout: 5000,
//   maximumAge: 0,
// };

// function success(pos) {
//   const crd = pos.coords;

//   console.log("Your current position is:");
//   console.log(`Latitude : ${crd.latitude}`);
//   console.log(`Longitude: ${crd.longitude}`);
//   console.log(`More or less ${crd.accuracy} meters.`);
// }

// function error(err) {
//   console.warn(`ERROR(${err.code}): ${err.message}`);
// }

// navigator.geolocation.getCurrentPosition(success, error, options);