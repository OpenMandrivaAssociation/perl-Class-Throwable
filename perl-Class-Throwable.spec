%define upstream_name    Class-Throwable
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	A minimal lightweight exception class
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildArch:	noarch

%description
This module implements a minimal lightweight exception object. It is meant to
be a compromise between more basic solutions like Carp which can only print
information and cannot handle exception objects, and more more complex
solutions like Exception::Class which can be used to define complex inline
exceptions and has a number of module dependencies.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Class/*

%clean
rm -rf $RPM_BUILD_ROOT

