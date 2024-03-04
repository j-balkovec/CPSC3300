/**
 * Redirects the user to the specified URL.
 * @param {string} url - The URL to redirect to.
 * @function redirectTo
 */
function redirectTo(url) {
  window.location.href = url;
}
    
/**
 * Displays the full name of a user based on their username.
 * @function displayFullName
 */
function displayFullName() {
  const usernameDiv = document.querySelector('.username');
  const usernameText = usernameDiv.textContent.trim();
  const atIndex = usernameText.indexOf('@'); 
  const username = atIndex !== -1 ? usernameText.slice(atIndex + 1) : usernameText;

  const userFullNames = {
      'ncole': 'Nicole O\'Riley',
      'robertocurry': 'Robert Curry',
      'johnsoneric': 'Eric Johnson',
      'kathleen22': 'Kathleen Smith',
      'burchjustin': 'Justin Burch',
      'hebertjessica': 'Jessica Hebert',
      'billywong': 'Wong Billy',
      'brittney21': 'Britney Spears',
      'wardoscar': 'Oscar Ward',
      'michael91': 'Michael Jackson',
      'benjamin': 'Benjamin Ragatron'
  };

  const fullName = userFullNames[username] || 'Unknown';

  const fullNameElement = document.getElementById('fullName');

  fullNameElement.textContent = fullName;
}

/**
 * Opens the search popup.
 * @function openSearchPopup
 */
function openSearchPopup() {
  var searchPopup = document.getElementById('searchPopup');
  searchPopup.style.display = 'block';
}

/**
 * Closes the search popup by hiding it.
 * @function closeSearchPopup
 */
function closeSearchPopup() {
  var searchPopup = document.getElementById('searchPopup');
  searchPopup.style.display = 'none';
}

/**
 * Performs a search using the provided search query.
 * Makes an AJAX request to the Flask server and updates the search results on the page.
 * @function performSearch
 */
function performSearch() {
  var searchQuery = document.getElementById("searchQuery").value;

  if (searchQuery === "") { return; }
  
  // Perform AJAX request to Flask server
  fetch('/search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ search_query: searchQuery })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.text();
  })
  .then(html => {
    document.getElementById("searchResults").innerHTML = html; 
  })
  .catch(error => {
    console.error('Error:', error); // Log any errors
  });
}







