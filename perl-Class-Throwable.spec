%define realname Class-Throwable
%define name	perl-%{realname}
%define version	0.10
%define release	%mkrel 1

Summary:	A minimal lightweight exception class
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		%{realname}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

%description
This module implements a minimal lightweight exception object. It is meant to
be a compromise between more basic solutions like Carp which can only print
information and cannot handle exception objects, and more more complex
solutions like Exception::Class which can be used to define complex inline
exceptions and has a number of module dependencies.

%prep
%setup -q -n %{realname}-%{version}

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

