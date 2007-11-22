Summary:	Gattrib for gEDA project
Summary(pl.UTF-8):	Gattrib dla projektu gEDA
Name:		geda-gattrib
Version:	1.2.0
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/release/v1.2/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	39acaa05c12c78f5a1fece22760e9d91
URL:		http://www.geda.seul.org/
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libgeda-devel >= %{version}
BuildRequires:	pkgconfig
Requires:	libgeda >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gattrib for the gEDA project.

%description -l pl.UTF-8
Gattrib dla projektu gEDA.

%prep
%setup -q

%build
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
#%%doc AUTHORS ChangeLog* NEWS README docs/README.*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gEDA/system-gattribrc
%{_datadir}/gEDA/gattrib-menus.xml
