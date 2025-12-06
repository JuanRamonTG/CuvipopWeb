// Sistema simple de autenticación basado en localStorage
// Cuando el usuario hace login, se guarda el token en localStorage

function isLoggedIn() {
    const token = localStorage.getItem('auth_token');
    return !!token && token.trim() !== '';
}

function getAuthToken() {
    return localStorage.getItem('auth_token') || null;
}

function setAuthToken(token) {
    localStorage.setItem('auth_token', token);
}

function logout() {
    localStorage.removeItem('auth_token');
    localStorage.removeItem('usuario');
    window.location.href = '/static/index.html';
}

function getCurrentUser() {
    return JSON.parse(localStorage.getItem('usuario')) || null;
}

function setCurrentUser(user) {
    localStorage.setItem('usuario', JSON.stringify(user));
}

// Exportar para uso global
window.authUtils = {
    isLoggedIn,
    getAuthToken,
    setAuthToken,
    logout,
    getCurrentUser,
    setCurrentUser
};
