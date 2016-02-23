%{?scl:%scl_package nodejs-asn1}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-asn1
Version:        0.1.11
Release:        4.1%{?dist}
Summary:        Contains parsers and serializers for ASN.1 (currently BER only)
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

Group:          System Environment/Libraries
License:        MIT
URL:            https://github.com/mcavage/node-asn1
Source0:        http://registry.npmjs.org/asn1/-/asn1-%{version}.tgz
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  %{?scl_prefix}nodejs-devel

#for tests
#BuildRequires:  %{?scl_prefix}npm(tap)

%description
nodejs-asn1 is a library for encoding and decoding Abstract Syntax Notation One
(ASN.1) datatypes in pure JavaScript. ASN.1 is  is a standard and notation that 
describes rules and structures for representing, encoding, transmitting, and 
decoding data in telecommunications and computer networking.

Currently Basic Encoding Rules (BER) encoding is supported; at some point 
Distinguished Encoding Rules (DER) will likely also be supported.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %buildroot

mkdir -p %{buildroot}%{nodejs_sitelib}/asn1
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/asn1

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
#%tap tst/ber/*.js

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/asn1
%doc LICENSE README.md

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.11-4.1
- rebuilt

* Wed Dec 11 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.11-3.1
- enable scl support

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-3
- restrict to compatible arches

* Fri Jun 21 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-2
- improve description

* Thu Jun 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.11-1
- initial package
