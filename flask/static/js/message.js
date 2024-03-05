document.addEventListener("DOMContentLoaded", function () {
  /**
   * Retrieves all elements with the class "message-timestamp" and stores them in a NodeList.
   * @type {NodeList}
   */
  const messageTimestamps = document.querySelectorAll(".message-timestamp");
  messageTimestamps.forEach(function (element) {
    const timestampString = element.dataset.timestamp;
    const timestamp = new Date(timestampString).getTime() / 1000;
    element.textContent = formatTimestamp(timestamp);
  });
});

/**
 * Formats a timestamp into a human-readable string representing the time difference from the current time.
 * @param {number} timestamp - The timestamp to format (in seconds).
 * @returns {string} The formatted timestamp.
 */
function formatTimestamp(timestamp) {
  const now = new Date();
  const messageTime = new Date(timestamp * 1000); // Multiply by 1000 to convert to milliseconds
  const difference = now - messageTime;

  const minute = 60 * 1000;
  const hour = minute * 60;
  const day = hour * 24;
  const week = day * 7;

  if (difference < minute) {
    return 'Just now';
  } else if (difference < hour) {
    const minutes = Math.floor(difference / minute);
    return minutes + 'm ago';
  } else if (difference < day) {
    const hours = Math.floor(difference / hour);
    return hours + 'h ago';
  } else if (difference < week) {
    const days = Math.floor(difference / day);
    return days + 'd ago';
  } else {
    return messageTime.toLocaleDateString(); // Display full date if older than a week
  }
}
