Summary:	Gattrib for gEDA project
Summary(pl.UTF-8):	Gattrib dla projektu gEDA
Name:		geda-gattrib
Version:	1.4.2
Release:	2
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/release/v1.4/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f5e85cceedb47b55437b8f14888d10cf
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
%configure \
	--disable-update-desktop-database
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_localedir}/{nl_NL,nl}
mv $RPM_BUILD_ROOT%{_localedir}/{de_DE,de}
mv $RPM_BUILD_ROOT%{_localedir}/{es_ES,es}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc AUTHORS ChangeLog* NEWS README docs/README.*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gEDA/system-gattribrc
%{_datadir}/gEDA/gattrib-menus.xml
