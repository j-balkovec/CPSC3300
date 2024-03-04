function redirectTo(url) {
  window.location.href = url;
}
    
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

function redirectTo(url) {
  window.location.href = url;
}

function openSearchPopup() {
  var searchPopup = document.getElementById('searchPopup');
  searchPopup.style.display = 'block';
}

function closeSearchPopup() {
  var searchPopup = document.getElementById('searchPopup');
  searchPopup.style.display = 'none';
}

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
    return response.text(); // Assuming the response is HTML
  })
  .then(html => {
    document.getElementById("searchResults").innerHTML = html; // Assuming you have a div with id "searchResults"
  })
  .catch(error => {
    console.error('Error:', error); // Log any errors
  });
}







