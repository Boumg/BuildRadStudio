#include <DUnitX.TestFramework.hpp>
#include <stdio.h>

#pragma option --xrtti

class __declspec(delphirtti) TMyTestObject : public TObject
{
public:
  virtual void __fastcall SetUp();
  virtual void __fastcall TearDown();

__published:
  void __fastcall Test1();
  void __fastcall Test2();
};


void __fastcall TMyTestObject::SetUp()
{
}

void __fastcall TMyTestObject::TearDown()
{
}

void __fastcall TMyTestObject::Test1()
{

  String s("Hello");
  Dunitx::Testframework::Assert::IsTrue(s == "Hello");
}

void __fastcall TMyTestObject::Test2()
{

  String s("Hello");
  Dunitx::Testframework::Assert::IsFalse(s == "Bonjour"); // This fails for illustrative purposes       but no
}

static void registerTests()
{
  TDUnitX::RegisterTestFixture(__classid(TMyTestObject));
}
#pragma startup registerTests 33