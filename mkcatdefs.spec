Name: mkcatdefs
Version: 1.0
Release: %mkrel 4
Summary: Catalog definition tool
Group: Sciences/Geosciences
URL: https://fdo.osgeo.org/
Source: %{name}-%{version}.tar.bz2
License: GPL
BuildRequires: cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Catalog definition tool splitted from fdo main source

%files
%defattr(-,root,root)
%{_bindir}/*

%prep
%setup -q

%build

%cmake
%make

%install
rm -rf %buildroot
make -C build DESTDIR=%buildroot install

%clean
rm -rf $RPM_BUILD_ROOT

