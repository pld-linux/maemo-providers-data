#
%define snap 20070601
Summary:	Maemo Data provider definitions
Name:		maemo-providers-data
Version:	0.0.%{snap}
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	c1ab996d299cd2cc10678ee797fb1097
URL:		http://modest.garage.maemo.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
#BuildRequires:	python-devel
#BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%package devel
Summary:	pkgconfig file for Maemo data provider definitions
Group:		Development/Libraries

%description devel
pkgconfig file for Maemo data provider definitions

%description
Data provider definitions for the Maemo platform

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/modest/provider-data
%{_datadir}/modest/provider-data/provider-data.keyfile

%files devel
%{_pkgconfigdir}/maemo-providers-data.pc
