%define upstream_name    Class-Throwable
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A minimal lightweight exception class
License:	Artistic/GPL
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Class/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 680828
- mass rebuild

* Mon Jul 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 400634
- update to 0.11
- using %%perl_convert_version
- fixed source field

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.10-4mdv2009.0
+ Revision: 256031
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.10-2mdv2008.1
+ Revision: 136685
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-2mdv2008.0
+ Revision: 86160
- rebuild


* Fri Mar 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-1mdk
- First Mandriva release

