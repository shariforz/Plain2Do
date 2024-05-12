import axios from "axios";
import swal from "sweetalert";
import { loginConfirmedAction, logout } from "../store/actions/AuthActions";

export function signUp(username, password) {
  //axios call
  const postData = {
    username,
    password,
    returnSecureToken: true,
  };
  return axios.post(
    `https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyD3RPAp3nuETDn9OQimqn_YF6zdzqWITII`,
    postData
  );
}

export function login(username, password) {
  const postData = {
    username,
    password,
  };
  return axios.post(`https://test.teamq.uz/api/token/`, postData);
}

export function formatError(errorResponse) {
  if (!errorResponse || !errorResponse.data || !errorResponse.data.error) {
    return "Unknown error occurred";
  }

  const message = errorResponse.data.error.message;
  swal("Oops", message, "error");
  return message; // Always return a string that can be handled by the Redux action.
}

export function saveTokenInLocalStorage(tokenDetails) {
  const expiresIn = tokenDetails.expiresIn || 3600; // default to 1 hour if not provided
  const expireDate = new Date(new Date().getTime() + expiresIn * 1000);
  console.log(tokenDetails);
  const detailsToStore = {
    accessToken: tokenDetails.access,
    refreshToken: tokenDetails.refresh,
    expireDate: expireDate,
  };

  localStorage.setItem("userDetails", JSON.stringify(detailsToStore));
}

export function runLogoutTimer(dispatch, timer, history) {
  setTimeout(() => {
    dispatch(logout(history));
  }, timer || 3600000); // Default to 1 hour if expiresIn is undefined
}

export function checkAutoLogin(dispatch, history) {
  const tokenDetailsString = localStorage.getItem("userDetails");
  let tokenDetails = "";
  if (!tokenDetailsString) {
    dispatch(logout(history));
    return;
  }

  tokenDetails = JSON.parse(tokenDetailsString);
  let expireDate = new Date(tokenDetails.expireDate);
  let todaysDate = new Date();

  if (todaysDate > expireDate) {
    dispatch(logout(history));
    return;
  }
  dispatch(loginConfirmedAction(tokenDetails));

  const timer = expireDate.getTime() - todaysDate.getTime();
  runLogoutTimer(dispatch, timer, history);
}
