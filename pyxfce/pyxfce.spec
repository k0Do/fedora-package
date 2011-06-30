%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}


Name:           pyxfce
Version:        4.6.0 
Release:        1%{?dist}
Summary:        Xfce bindings for Python
Group:          Development/Languages
License:        BSD
URL:            http://pyxfce.xfce.org
Source0:        http://pyxfce.xfce.org/pyxfce-%{version}.tar.gz

BuildRequires:  libxfcegui4-devel
BuildRequires:  libxfce4menu-devel
BuildRequires:  python-devel
BuildRequires:  pygtk2-devel

%description
pyxfce are Xfce bindings for Python. 
You can use Python to create Xfce programs, after you installed pyxfce.

%package devel
Summary: Development files for building add-on libraries
Group: Development/Languages
Requires: %{name} = %{version}-%{release}

%description devel
This package contains files required to build wrappers for Xfce add-on
libraries so that they interoperate with pyxfce.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)
%doc README TODO COPYING ChangeLog AUTHORS
%{python_sitearch}/xfce4/

%files devel
%{_datadir}/%{name}/
%{_libdir}/pkgconfig/pyxfce-1.0.pc


%changelog
* Thu Jun 30 2011 Raphael Groner <raphgro-at-web.de> 4.6.0-1
- Initial version
