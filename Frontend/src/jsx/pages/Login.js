import React, { useState } from "react";
import { connect, useDispatch } from "react-redux";
import { Link } from "react-router-dom";
import {
  loadingToggleAction,
  loginAction,
} from "../../store/actions/AuthActions";

// image
import logo from "../../images/plain2do.png";
import loginbg from "../../images/bg-login.jpg";

function Login(props) {
  const [username, setUsername] = useState("admin");
  const [password, setPassword] = useState("admin123");
  let errorsObj = { username: "", password: "" };
  const [errors, setErrors] = useState(errorsObj);

  const dispatch = useDispatch();

  function onLogin(e) {
    e.preventDefault();
    let error = false;
    const errorObj = { ...errorsObj };
    if (username === "") {
      errorObj.username = "username is Required";
      error = true;
    }
    if (password === "") {
      errorObj.password = "Password is Required";
      error = true;
    }
    setErrors(errorObj);
    if (error) {
      return;
    }
    dispatch(loadingToggleAction(true));
    dispatch(loginAction(username, password, props.history));
  }

  return (
    <div
      className="login-main-page"
      style={{ backgroundImage: "url(" + loginbg + ")" }}
    >
      <div className="login-wrapper">
        <div className="login-aside-left">
          <Link to="/dashboard" className="login-logo">
            <img src={logo} width={200} alt="" />
          </Link>
          <div className="login-description">
            <h2 className="main-title mb-2">Welcome To Plain2do</h2>
            <p className="">
              It is a long established fact that a reader will be distracted by
              the readable content of a page when looking at its layout. The
              point of using Lorem Ipsum is that it has a more-or-less normal
              distribution of letters,
            </p>
            <ul className="social-icons mt-4">
              <li>
                <Link to={"#"}>
                  <i className="fa fa-facebook"></i>
                </Link>
              </li>
              <li>
                <Link to={"#"}>
                  <i className="fa fa-twitter"></i>
                </Link>
              </li>
              <li>
                <Link to={"#"}>
                  <i className="fa fa-linkedin"></i>
                </Link>
              </li>
            </ul>
            <div className="mt-5 bottom-privacy"></div>
          </div>
        </div>
        <div className="login-aside-right">
          <div className="row m-0 justify-content-center h-100 align-items-center">
            <div className="p-5">
              <div className="authincation-content">
                <div className="row no-gutters">
                  <div className="col-xl-12">
                    <div className="auth-form-1">
                      <div className="mb-4">
                        <h3 className="dz-title mb-1">Sign in</h3>
                        <p className="">
                          Sign in by entering information below
                        </p>
                      </div>
                      {props.errorMessage && (
                        <div className="bg-red-300 text-red-900 border border-red-900 p-1 my-2">
                          {props.errorMessage}
                        </div>
                      )}
                      {props.successMessage && (
                        <div className="bg-green-300 text-green-900 border border-green-900 p-1 my-2">
                          {props.successMessage}
                        </div>
                      )}
                      <form onSubmit={onLogin}>
                        <div className="form-group">
                          <label className="mb-2 ">
                            <strong>username</strong>
                          </label>
                          <input
                            className="form-control"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="Type Your username Address"
                          />
                          {errors.username && (
                            <div className="text-danger fs-12">
                              {errors.username}
                            </div>
                          )}
                        </div>
                        <div className="form-group">
                          <label className="mb-2 ">
                            <strong>Password</strong>
                          </label>
                          <input
                            type="password"
                            className="form-control"
                            value={password}
                            placeholder="Type Your Password"
                            onChange={(e) => setPassword(e.target.value)}
                          />
                          {errors.password && (
                            <div className="text-danger fs-12">
                              {errors.password}
                            </div>
                          )}
                        </div>
                        <div className="form-row d-flex justify-content-between mt-4 mb-2">
                          <div className="form-group">
                            <div className="custom-control custom-checkbox ml-1 ">
                              <input
                                type="checkbox"
                                className="custom-control-input"
                                id="basic_checkbox_1"
                              />
                              <label
                                className="custom-control-label"
                                htmlFor="basic_checkbox_1"
                              >
                                Remember my preference
                              </label>
                            </div>
                          </div>
                        </div>
                        <div className="text-center">
                          <button
                            type="submit"
                            className="btn btn-block btn-purple text-white"
                          >
                            Sign In
                          </button>
                        </div>
                      </form>
                      <div className="new-account mt-2">
                        <p className="">
                          Don't have an account?{" "}
                          <Link className="text__purple" to="./page-register">
                            Sign up
                          </Link>
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

const mapStateToProps = (state) => {
  return {
    errorMessage: state.auth.errorMessage,
    successMessage: state.auth.successMessage,
    showLoading: state.auth.showLoading,
  };
};
export default connect(mapStateToProps)(Login);
