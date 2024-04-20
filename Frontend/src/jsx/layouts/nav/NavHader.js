import React, { Fragment, useContext, useState } from "react";
/// React router dom
import { Link } from "react-router-dom";
import { ThemeContext } from "../../../context/ThemeContext";

const NavHader = () => {
  const [toggle, setToggle] = useState(false);
  const { navigationHader, openMenuToggle, background } =
    useContext(ThemeContext);
  return (
    <div className="nav-header">
      <Link to="/dashboard" className="brand-logo">
        {background.value === "dark" || navigationHader !== "color_1" ? (
          <Fragment>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="60"
              viewBox="0 0 54.613 42.998"
            >
              <defs>
                <linearGradient
                  id="linear-gradient"
                  x1="0.518"
                  y1="0.554"
                  x2="0.706"
                  y2="0.086"
                  gradientUnits="objectBoundingBox"
                >
                  <stop offset="0" stop-color="#56006e" stop-opacity="0" />
                  <stop offset="1" stop-color="#56006e" />
                </linearGradient>
              </defs>
              <g
                id="Сгруппировать_1"
                data-name="Сгруппировать 1"
                transform="translate(-67.158 -336.527)"
              >
                <path
                  id="Контур_1"
                  data-name="Контур 1"
                  d="M170.058,379.518H157.224l12.748-25.827s5.317-.97,6.843,3.82l-6.161,11.362a10.73,10.73,0,0,0,10.354-10.764,10.962,10.962,0,0,0-10.95-10.95H155.912v32.358H145.281V336.527h24.777a21.605,21.605,0,0,1,21.581,21.581,21.182,21.182,0,0,1-6.348,15.2A21.556,21.556,0,0,1,170.058,379.518Z"
                  transform="translate(-69.868)"
                  fill="#8e00af"
                />
                <path
                  id="Контур_2"
                  data-name="Контур 2"
                  d="M308.947,513.42l6.135-11.313c-1.526-4.79-6.843-3.82-6.843-3.82l-8.356,16.929,6.255.426Z"
                  transform="translate(-208.135 -144.596)"
                  fill="url(#linear-gradient)"
                />
                <path
                  id="Контур_3"
                  data-name="Контур 3"
                  d="M106.945,476.191s-1.279-3.645-6.759-1.3c-6.936,2.966-19.649,23.3-19.649,23.3l-13.38-19.816,6.691-5.032,6.672,10.871s8.628-12.541,15.829-14.475c5.739-1.541,8.37.571,9.576,2.781A8.9,8.9,0,0,1,106.945,476.191Z"
                  transform="translate(0 -118.659)"
                  fill="#7bb300"
                />
              </g>
            </svg>
            <svg className="brand-title" width="124px" height="33px">
              <g
                id="Сгруппировать_2"
                data-name="Сгруппировать 2"
                transform="translate(-632.267 -504.429)"
              >
                <path
                  id="Контур_4"
                  data-name="Контур 4"
                  d="M641.033,509.584c4.353-.009,7.269,2.237,7.277,6.559.009,4.353-2.9,6.58-7.251,6.589l-5.044.01.015,7.625-3.723.007-.041-20.773Zm-5.054,9.886,5.133-.01c2.191,0,3.66-1.058,3.656-3.279,0-2.192-1.477-3.209-3.669-3.2l-5.134.01Z"
                  transform="translate(0 -3.52)"
                  fill="#fff"
                />
                <path
                  id="Контур_5"
                  data-name="Контур 5"
                  d="M696.981,505.046l.044,22.185-3.482.007-.042-21.014Z"
                  transform="translate(-41.815 -0.421)"
                  fill="#fff"
                />
                <path
                  id="Контур_6"
                  data-name="Контур 6"
                  d="M717.809,524.781a9.7,9.7,0,0,1,5.791-1.722c3.692-.007,6.308,1.519,6.317,6.321l.02,10.117-3.212.006,0-.991a8.385,8.385,0,0,1-4.41,1.21c-3.182.007-5.706-1.61-5.714-5.123-.007-3.542,2.541-5.408,6.083-5.415a10.251,10.251,0,0,1,3.814.712c-.006-2.912-1.208-3.569-3.249-3.566a7,7,0,0,0-4.081,1.208Zm8.7,11.391-.008-4.023a11.15,11.15,0,0,0-2.973-.444c-2.041,0-3.691.788-3.687,2.679,0,1.8,1.506,2.489,3.277,2.486A9.509,9.509,0,0,0,726.507,536.172Z"
                  transform="translate(-57.587 -12.722)"
                  fill="#fff"
                />
                <path
                  id="Контур_7"
                  data-name="Контур 7"
                  d="M775.586,506.406a1.908,1.908,0,1,1-1.925-1.977A1.86,1.86,0,0,1,775.586,506.406Zm-.141,4.294.032,16.061-3.482.006-.032-16.06Z"
                  transform="translate(-95.265 0)"
                  fill="#fff"
                />
                <path
                  id="Контур_8"
                  data-name="Контур 8"
                  d="M800.813,523.294l0,1.711a5.949,5.949,0,0,1,4.769-2.111c3.212-.007,5.407,1.79,5.416,6.264l.02,10.176-3.482.006-.019-9.786c-.005-2.462-1.208-3.389-3.069-3.386a3.428,3.428,0,0,0-3.417,2.378l.022,10.807-3.483.007L797.54,523.3Z"
                  transform="translate(-112.86 -12.609)"
                  fill="#fff"
                />
                <path
                  id="Контур_9"
                  data-name="Контур 9"
                  d="M851.47,511.606a8.547,8.547,0,0,1,7.288-3.676c3.723-.008,6.938,1.908,6.947,6.08a5.212,5.212,0,0,1-2.333,4.567c-1.708,1.265-4.408,2.23-6.177,3.465a4.084,4.084,0,0,0-2.063,3.757l10.537-.021.007,3.3-14.47.028,0-1.111c-.007-3.212.619-5.674,2.628-7.42,1.737-1.5,4.827-2.651,6.417-3.555,1.469-.843,2.038-1.656,2.036-2.916,0-2.011-1.477-2.909-3.4-2.905a6.288,6.288,0,0,0-5.068,2.712Z"
                  transform="translate(-149.504 -2.391)"
                  fill="#fff"
                />
                <path
                  id="Контур_10"
                  data-name="Контур 10"
                  d="M915.6,509.053c6.184-.012,10.995,3.911,11.007,10.3.013,6.424-4.842,10.456-10.965,10.469l-6.214.012-.041-20.773Zm-2.428,17.326,2.492-.005c3.993-.008,7.2-2.536,7.191-6.979-.009-4.383-3.225-6.9-7.218-6.89l-2.492.005Z"
                  transform="translate(-189.233 -3.158)"
                  fill="#fff"
                />
                <path
                  id="Контур_11"
                  data-name="Контур 11"
                  d="M983.3,530.943c.011,5.524-2.835,8.441-6.828,8.449-4.052.008-6.88-2.9-6.891-8.423-.011-5.493,2.835-8.41,6.858-8.418C980.4,522.543,983.291,525.449,983.3,530.943Zm-10.416.051c.007,3.422,1.421,5.221,3.582,5.217,2.1,0,3.569-1.809,3.562-5.231-.006-3.452-1.481-5.221-3.583-5.216C974.316,525.768,972.879,527.541,972.885,530.993Z"
                  transform="translate(-230.343 -12.375)"
                  fill="#fff"
                />
              </g>
            </svg>
          </Fragment>
        ) : (
          <Fragment>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="60"
              viewBox="0 0 54.613 42.998"
            >
              <defs>
                <linearGradient
                  id="linear-gradient"
                  x1="0.518"
                  y1="0.554"
                  x2="0.706"
                  y2="0.086"
                  gradientUnits="objectBoundingBox"
                >
                  <stop offset="0" stop-color="#56006e" stop-opacity="0" />
                  <stop offset="1" stop-color="#56006e" />
                </linearGradient>
              </defs>
              <g
                id="Сгруппировать_1"
                data-name="Сгруппировать 1"
                transform="translate(-67.158 -336.527)"
              >
                <path
                  id="Контур_1"
                  data-name="Контур 1"
                  d="M170.058,379.518H157.224l12.748-25.827s5.317-.97,6.843,3.82l-6.161,11.362a10.73,10.73,0,0,0,10.354-10.764,10.962,10.962,0,0,0-10.95-10.95H155.912v32.358H145.281V336.527h24.777a21.605,21.605,0,0,1,21.581,21.581,21.182,21.182,0,0,1-6.348,15.2A21.556,21.556,0,0,1,170.058,379.518Z"
                  transform="translate(-69.868)"
                  fill="#8e00af"
                />
                <path
                  id="Контур_2"
                  data-name="Контур 2"
                  d="M308.947,513.42l6.135-11.313c-1.526-4.79-6.843-3.82-6.843-3.82l-8.356,16.929,6.255.426Z"
                  transform="translate(-208.135 -144.596)"
                  fill="url(#linear-gradient)"
                />
                <path
                  id="Контур_3"
                  data-name="Контур 3"
                  d="M106.945,476.191s-1.279-3.645-6.759-1.3c-6.936,2.966-19.649,23.3-19.649,23.3l-13.38-19.816,6.691-5.032,6.672,10.871s8.628-12.541,15.829-14.475c5.739-1.541,8.37.571,9.576,2.781A8.9,8.9,0,0,1,106.945,476.191Z"
                  transform="translate(0 -118.659)"
                  fill="#7bb300"
                />
              </g>
            </svg>

            <svg className="brand-title" width="124px" height="33px">
              <g
                id="Сгруппировать_2"
                data-name="Сгруппировать 2"
                transform="translate(-632.267 -504.429)"
              >
                <path
                  id="Контур_4"
                  data-name="Контур 4"
                  d="M641.033,509.584c4.353-.009,7.269,2.237,7.277,6.559.009,4.353-2.9,6.58-7.251,6.589l-5.044.01.015,7.625-3.723.007-.041-20.773Zm-5.054,9.886,5.133-.01c2.191,0,3.66-1.058,3.656-3.279,0-2.192-1.477-3.209-3.669-3.2l-5.134.01Z"
                  transform="translate(0 -3.52)"
                />
                <path
                  id="Контур_5"
                  data-name="Контур 5"
                  d="M696.981,505.046l.044,22.185-3.482.007-.042-21.014Z"
                  transform="translate(-41.815 -0.421)"
                />
                <path
                  id="Контур_6"
                  data-name="Контур 6"
                  d="M717.809,524.781a9.7,9.7,0,0,1,5.791-1.722c3.692-.007,6.308,1.519,6.317,6.321l.02,10.117-3.212.006,0-.991a8.385,8.385,0,0,1-4.41,1.21c-3.182.007-5.706-1.61-5.714-5.123-.007-3.542,2.541-5.408,6.083-5.415a10.251,10.251,0,0,1,3.814.712c-.006-2.912-1.208-3.569-3.249-3.566a7,7,0,0,0-4.081,1.208Zm8.7,11.391-.008-4.023a11.15,11.15,0,0,0-2.973-.444c-2.041,0-3.691.788-3.687,2.679,0,1.8,1.506,2.489,3.277,2.486A9.509,9.509,0,0,0,726.507,536.172Z"
                  transform="translate(-57.587 -12.722)"
                />
                <path
                  id="Контур_7"
                  data-name="Контур 7"
                  d="M775.586,506.406a1.908,1.908,0,1,1-1.925-1.977A1.86,1.86,0,0,1,775.586,506.406Zm-.141,4.294.032,16.061-3.482.006-.032-16.06Z"
                  transform="translate(-95.265 0)"
                />
                <path
                  id="Контур_8"
                  data-name="Контур 8"
                  d="M800.813,523.294l0,1.711a5.949,5.949,0,0,1,4.769-2.111c3.212-.007,5.407,1.79,5.416,6.264l.02,10.176-3.482.006-.019-9.786c-.005-2.462-1.208-3.389-3.069-3.386a3.428,3.428,0,0,0-3.417,2.378l.022,10.807-3.483.007L797.54,523.3Z"
                  transform="translate(-112.86 -12.609)"
                />
                <path
                  id="Контур_9"
                  data-name="Контур 9"
                  d="M851.47,511.606a8.547,8.547,0,0,1,7.288-3.676c3.723-.008,6.938,1.908,6.947,6.08a5.212,5.212,0,0,1-2.333,4.567c-1.708,1.265-4.408,2.23-6.177,3.465a4.084,4.084,0,0,0-2.063,3.757l10.537-.021.007,3.3-14.47.028,0-1.111c-.007-3.212.619-5.674,2.628-7.42,1.737-1.5,4.827-2.651,6.417-3.555,1.469-.843,2.038-1.656,2.036-2.916,0-2.011-1.477-2.909-3.4-2.905a6.288,6.288,0,0,0-5.068,2.712Z"
                  transform="translate(-149.504 -2.391)"
                />
                <path
                  id="Контур_10"
                  data-name="Контур 10"
                  d="M915.6,509.053c6.184-.012,10.995,3.911,11.007,10.3.013,6.424-4.842,10.456-10.965,10.469l-6.214.012-.041-20.773Zm-2.428,17.326,2.492-.005c3.993-.008,7.2-2.536,7.191-6.979-.009-4.383-3.225-6.9-7.218-6.89l-2.492.005Z"
                  transform="translate(-189.233 -3.158)"
                />
                <path
                  id="Контур_11"
                  data-name="Контур 11"
                  d="M983.3,530.943c.011,5.524-2.835,8.441-6.828,8.449-4.052.008-6.88-2.9-6.891-8.423-.011-5.493,2.835-8.41,6.858-8.418C980.4,522.543,983.291,525.449,983.3,530.943Zm-10.416.051c.007,3.422,1.421,5.221,3.582,5.217,2.1,0,3.569-1.809,3.562-5.231-.006-3.452-1.481-5.221-3.583-5.216C974.316,525.768,972.879,527.541,972.885,530.993Z"
                  transform="translate(-230.343 -12.375)"
                />
              </g>
            </svg>
          </Fragment>
        )}
      </Link>

      <div
        className="nav-control"
        onClick={() => {
          setToggle(!toggle);
          openMenuToggle();
        }}
      >
        <div className={`hamburger ${toggle ? "is-active" : ""}`}>
          <span className="line"></span>
          <span className="line"></span>
          <span className="line"></span>
        </div>
      </div>
    </div>
  );
};

export default NavHader;