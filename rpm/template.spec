Name:           ros-indigo-world-canvas-client-examples
Version:        0.1.0
Release:        1%{?dist}
Summary:        ROS world_canvas_client_examples package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/world_canvas_client_examples
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-unique-id
Requires:       ros-indigo-uuid-msgs
Requires:       ros-indigo-world-canvas-client-cpp
Requires:       ros-indigo-world-canvas-client-py
Requires:       ros-indigo-world-canvas-msgs
Requires:       ros-indigo-yocs-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-unique-id
BuildRequires:  ros-indigo-uuid-msgs
BuildRequires:  ros-indigo-world-canvas-client-cpp
BuildRequires:  ros-indigo-world-canvas-msgs
BuildRequires:  ros-indigo-yocs-msgs

%description
Examples showing how to use C++ and Python client libraries to access semantic
maps within the world canvas framework.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Nov 29 2014 Jorge Santos <jsantossimon@gmail.com> - 0.1.0-1
- Autogenerated by Bloom

* Fri Nov 28 2014 Jorge Santos <jsantossimon@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

