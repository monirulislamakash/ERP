// Attendance Oprations
let markAttendance = () => {
  let progressBar = document.querySelector('.progress-bar');
  document.getElementById('Mark_AttendanceText').innerText = "please wait...";
  document.getElementById('progress').style.display = "block";
  progressBar.style.width = '0%'; // Reset progress bar

  document.getElementById('Mark_AttendanceText').innerText = "Marking attendance...";
  setTimeout(() => {
    progressBar.style.width = '100%';
  }, 200);
  setTimeout(() => {
    document.getElementById('submitFrom').submit();
  }, 2000);
};
// Acction Opration
let toaster = () => {
  let toast = document.querySelector('.toast')
  toast.style.display = "none";
}
setTimeout(() => {
  let toast = document.querySelector('.toast')
  toast.style.display = "none";
}, 5000)

// Seclect Leave Option
// Wait for the DOM to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {
  // Get the select element and all content divs
  const selectElement = document.getElementById('contentSelector');
  const contentDivs = document.querySelectorAll('#contentContainer > div');

  /**
   * Handles the change event on the select element.
   * It hides all content divs and then shows the one corresponding to the selected option.
   */
  const handleSelectChange = () => {
    // Get the value of the currently selected option
    const selectedValue = selectElement.value;

    // Loop through all content divs and hide them
    contentDivs.forEach(div => {
      div.style.display = 'none';
    });

    // If a valid option is selected (not 'none'), show the corresponding div
    if (selectedValue !== 'none') {
      const selectedContentDiv = document.getElementById(selectedValue);
      if (selectedContentDiv) {
        selectedContentDiv.style.display = 'block';
      }
    }
  };

  // Add the change event listener to the select element
  selectElement.addEventListener('change', handleSelectChange);
});